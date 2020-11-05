declare function local:show_cursos() as element()*
{
  for $c in collection("cursosUA")//curso
  return 
  <elem>
    { $c/guid }
    { $c/nome }
  </elem>
};

<root>
{ local:show_cursos() }
</root>