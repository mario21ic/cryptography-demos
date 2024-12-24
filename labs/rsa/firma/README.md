Generar keys:
```
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```

Firmado:
```
echo "secreto" > mensaje.txt

openssl dgst -sign private.pem -keyform PEM -sha256 -out mensaje.txt.sign mensaje.txt
openssl dgst -verify public.pem -keyform PEM -sha256 -signature mensaje.txt.sign mensaje.txt
```
