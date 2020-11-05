let $cs := doc('cursosUA')//curso
for $c in $cs where $c/guid = '2'
return delete node $c