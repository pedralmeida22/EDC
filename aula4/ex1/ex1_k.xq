<root>{
  for $l in distinct-values(collection("cursosUA")//local)   
  return 
  <elem>
    <local>{$l}</local>
    {
      for $c in collection('cursosUA')//curso[local/text()=$l]
      return 
        <curso>{$c/nome/text()}</curso>
    }
  </elem>
}</root>