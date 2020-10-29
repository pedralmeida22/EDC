<root>{
  for $c in collection("cursosUA")//curso
  where $c/guid = 15
  return 
  <elem>
    {$c/nome}
    {$c/codigo}
    {$c/grau}
    {$c/local}
  </elem>
}</root>