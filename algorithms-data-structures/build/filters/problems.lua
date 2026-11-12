-- Turns source/problems.md into either the student answer sheets or the instructor key.
-- Set the mode with: pandoc ... -M mode=board   or   -M mode=key
--
-- Each problem in the source starts with a level-1 heading such as
--   # Running Sum of 1d Array {.problem number="1480" classno="1" slot="A"
--      level="Easy" topic="Big-O and Python memory" url="https://..." lines="12"}
-- and is followed by three divs: ::: statement, ::: memory, ::: key.
-- This filter only arranges those blocks and adds the blank answer template.
-- It writes no course text beyond the fixed field labels on the answer sheet.

local PAGEBREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
local NBSP = '\u{00A0}'

local function styled(style, inlines)
  return pandoc.Div({ pandoc.Para(inlines) }, pandoc.Attr('', {}, { { 'custom-style', style } }))
end

local function words(s)
  return pandoc.Inlines({ pandoc.Str(s) })
end

local function slot_label(slot)
  if slot == 'A' then return 'Problem A, the easier problem' end
  return 'Problem B, the harder problem'
end

local function unwrap(div, style)
  if not style then return div.content end
  local out = {}
  for _, b in ipairs(div.content) do
    if b.t == 'Para' or b.t == 'Plain' then
      table.insert(out, styled(style, b.content))
    else
      table.insert(out, b)
    end
  end
  return out
end

local function header_blocks(h, mode)
  local a = h.attributes
  local blocks = { pandoc.RawBlock('openxml', PAGEBREAK) }
  if mode == 'board' then
    table.insert(blocks, styled('Sheet Header', words(
      'Name ______________________________    Date ______________    Class '
      .. a.classno .. ', Problem ' .. a.slot)))
  end
  table.insert(blocks, styled('Problem Label', words(
    'Class ' .. a.classno .. ': ' .. a.topic .. '. ' .. slot_label(a.slot) .. '.')))
  local title = pandoc.Header(1, words('#' .. a.number .. ' ' .. pandoc.utils.stringify(h.content)))
  table.insert(blocks, title)
  local level_line = pandoc.Inlines({ pandoc.Strong(words(a.level .. '.')), pandoc.Space(),
    pandoc.Link(words(a.url), a.url) })
  table.insert(blocks, styled('Level Line', level_line))
  return blocks
end

local function answer_template(h, memory_div)
  local n = tonumber(h.attributes.lines or '10')
  local blocks = {}
  table.insert(blocks, pandoc.Header(3, words('Your Python solution')))
  for _ = 1, n do
    table.insert(blocks, styled('Answer Line', words(NBSP)))
  end
  table.insert(blocks, styled('Answer Field', words('Time complexity:')))
  table.insert(blocks, styled('Answer Field', words('Auxiliary space:')))
  if memory_div then
    for _, b in ipairs(unwrap(memory_div, 'Small Print')) do table.insert(blocks, b) end
  end
  table.insert(blocks, styled('Answer Field', words('Memory used by the input, in bytes:')))
  table.insert(blocks, styled('Answer Field', words('Memory used by your auxiliary data, in bytes:')))
  table.insert(blocks, styled('Answer Field', words('Total memory, in bytes:')))
  table.insert(blocks, styled('Answer Field', words('If you asked for help, write your two failed attempts here first.')))
  table.insert(blocks, styled('Answer Line', words('1.')))
  table.insert(blocks, styled('Answer Line', words('2.')))
  return blocks
end

function Pandoc(doc)
  local mode = pandoc.utils.stringify(doc.meta.mode or 'key')
  local out = {}
  local current, statement, memory, key = nil, nil, nil, nil

  local function flush()
    if not current then return end
    for _, b in ipairs(header_blocks(current, mode)) do table.insert(out, b) end
    if statement then
      for _, b in ipairs(unwrap(statement)) do table.insert(out, b) end
    end
    if mode == 'board' then
      for _, b in ipairs(answer_template(current, memory)) do table.insert(out, b) end
    else
      if memory then
        local mem = {}
        for _, b in ipairs(unwrap(memory, 'Small Print')) do table.insert(mem, b) end
        for _, b in ipairs(mem) do table.insert(out, b) end
      end
      if key then
        for _, b in ipairs(unwrap(key)) do table.insert(out, b) end
      end
    end
    current, statement, memory, key = nil, nil, nil, nil
  end

  for _, b in ipairs(doc.blocks) do
    if b.t == 'Header' and b.level == 1 and b.classes:includes('problem') then
      flush()
      current = b
    elseif current and b.t == 'Div' and b.classes:includes('statement') then
      statement = b
    elseif current and b.t == 'Div' and b.classes:includes('memory') then
      memory = b
    elseif current and b.t == 'Div' and b.classes:includes('key') then
      key = b
    elseif current then
      -- Anything else inside a problem belongs to the key only.
      if mode ~= 'board' then
        key = key or pandoc.Div({})
        table.insert(key.content, b)
      end
    else
      table.insert(out, b)
    end
  end
  flush()
  doc.blocks = out
  return doc
end
