<root>{
  for $d in distinct-values(collection("cursosUA")//departamento)   
  return 
  <elem>
    <departamento>{$d}</departamento>
    {
      for $c in collection('cursosUA')//curso[departamentos/departamento/text()=$d]
      return 
        <curso>{$c/nome/text()}</curso>
    }
  </elem>
}</root>