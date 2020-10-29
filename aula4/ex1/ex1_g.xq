<root>{
  for $c in collection("cursosUA")//curso
  where $c/guid = 15
   
  return 
  <elem>
    {$c//areacientifica}
  </elem>
}</root>