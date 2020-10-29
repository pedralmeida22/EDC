<root>{
  for $a in distinct-values(collection("cursosUA")//areacientifica)   
  return 
  <elem>
    <areacientifica>{$a}</areacientifica>
    {
      for $c in collection('cursosUA')//curso[areascientificas/areacientifica/text()=$a]
      return 
        <curso>{$c/nome/text()}</curso>
    }
  </elem>
}</root>