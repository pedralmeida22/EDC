<root>{
  for $c in collection("cursosUA")//curso
  where $c//areacientifica = "Biologia"
   
  return 
  <elem>
    {$c/nome}
  </elem>
}</root>