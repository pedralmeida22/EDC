<root>{
  for $c in collection("cursosUA")//curso
  where $c/guid = 15
   
  return 
  <elem>
    {$c/departamentos//departamento}
  </elem>
}</root>