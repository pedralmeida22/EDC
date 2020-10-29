<root>{
  let $d := collection("cursosUA")//curso//departamentos
  for $s in distinct-values($d/departamento)
  return 
    <elem>
      { $s }
    </elem>
}</root>