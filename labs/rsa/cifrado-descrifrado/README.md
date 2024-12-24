Generar keys:
```
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```

Cifrado y descifrado:
```
echo "secreto" > mensaje.txt

openssl pkeyutl -encrypt -pubin -inkey public.pem -in mensaje.txt -out mensaje_crifado.txt
openssl pkeyutl -decrypt -inkey private.pem -in mensaje_crifado.txt -out mensaje_descifrado.txt
```
