<root>{
  (:
  let $c := collection("cursosUA")//curso
  for $d in distinct-values($c/local)
  return 
    <elem>
      { $d }
    </elem>
  :)
  
  for $d in distinct-values(doc("cursosUA")//local)
  return 
    <elem>{ $d }</elem>
}</root>
