python3 -m http.server

podemos hace run filtro de packs de Bienvenida en Javascript

de Base de Datos ya tenemos el esquema hecho, nos hace falta el usuario y los permisos

Nadie se va a creer lo que he hecho!!!

hice los commits sin querer con la cuenta personal, claro tenog que hacerlo con la educativa y los commits ya se hicieron asi que tendría que cambiar el author de cada commit, suena sencillo pero ha sido un dolor de cabeza.

Pero "git rebase" viene a la salvación

"git rebase -i --root" para poder cambiar commit a commit desde el inicio hasta el final pudiendo cambiar el autor, el pusher, el propietario, el comentario, la fecha, etcétara, un monstruo de comando, si se usa bien arreglas cagadas como la mía, 1 hora para entender como se usa, y una vez finalizado haces "git switch -c "new-master"" liminas la anterior "git -D master" y cambias el nombre de esta a esta para hacer el cmabiazo "git -M master" y voilá, el asesianto perfecto, sin pruebas ni nada xD.
