declare updating function local:add-curso($guid, $name)
{
  let $c := collection('cursosUA')/cursos
  return insert nodes(
  <curso>
    <guid>{$guid}</guid>
    <nome>{$name}</nome>
  </curso>
) as first into $c
};

local:add-curso(2, 'inserted_udf')
