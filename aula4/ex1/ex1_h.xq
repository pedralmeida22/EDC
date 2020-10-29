<root>{
  for $c in collection("cursosUA")//curso
  where $c/local = "Campus Universitário de Santiago, Aveiro"
   
  return 
  <elem>
    {$c/nome}
  </elem>
}</root>