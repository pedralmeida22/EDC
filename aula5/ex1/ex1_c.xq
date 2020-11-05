let $cs := doc('cursosUA')//curso
for $c in $cs where $c/guid = 1
return replace node $c/nome/text() with 'edited'