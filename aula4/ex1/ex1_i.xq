<root>{
  for $c in collection("cursosUA")//curso
  where $c//departamento = "Departamento de Biologia"
   
  return 
  <elem>
    {$c/nome}
  </elem>
}</root>