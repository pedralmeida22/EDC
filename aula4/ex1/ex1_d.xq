<root>{
  let $d := collection("cursosUA")//curso//areascientificas
  for $s in distinct-values($d/areacientifica)
  return 
    <elem>
      { $s }
    </elem>
}</root>