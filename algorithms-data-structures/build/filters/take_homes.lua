-- Arranges source/take_homes.md. No course text is written here.
-- The planning steps are written once, in a div with id "standard-plan".
-- Each take-home marks where they go with an empty div of class "plan".
-- Every level-1 heading starts a new page, and the plan starts the back of the
-- sheet, so each take-home prints as one two-sided sheet.

local PAGEBREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

function Pandoc(doc)
  local plan = nil
  for _, b in ipairs(doc.blocks) do
    if b.t == 'Div' and b.identifier == 'standard-plan' then plan = b.content end
  end
  local out = {}
  local seen_h1 = false
  for _, b in ipairs(doc.blocks) do
    if b.t == 'Div' and b.identifier == 'standard-plan' then
      -- written once; placed below
    elseif b.t == 'Div' and b.classes:includes('plan') then
      -- The plan and the questions go on the back of the sheet.
      table.insert(out, pandoc.RawBlock('openxml', PAGEBREAK))
      for _, p in ipairs(plan or {}) do table.insert(out, p) end
    elseif b.t == 'Header' and b.level == 1 then
      table.insert(out, pandoc.RawBlock("openxml", PAGEBREAK))
      seen_h1 = true
      table.insert(out, b)
    else
      table.insert(out, b)
    end
  end
  doc.blocks = out
  return doc
end
