-- Layout helpers shared by every document. No course text is written here.
-- A paragraph that is only \newpage, or a div with class "pagebreak", becomes a Word page break.

local PAGEBREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

function Para(el)
  if #el.content == 1 and el.content[1].t == 'RawInline' and el.content[1].text == '\\newpage' then
    return pandoc.RawBlock('openxml', PAGEBREAK)
  end
  if #el.content == 1 and el.content[1].t == 'Str' and el.content[1].text == '\\newpage' then
    return pandoc.RawBlock('openxml', PAGEBREAK)
  end
end

function Div(el)
  if el.classes:includes('pagebreak') then
    return pandoc.RawBlock('openxml', PAGEBREAK)
  end
end
