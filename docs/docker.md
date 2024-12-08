## Docker Kurulumu
> Sunucuya SSH ile bağlandıktan sonra

### 1) Sistem güncellemesi:
```
sudo apt-get update && sudo apt-get upgrade -y
```

### 2) Docker GPG Anahtarının eklenmesi:
```
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

### 3) Docker Kaynağının Kütüphaneye Eklenmesi ve  Güncellenmesi:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### 4) Docker ve Diğer Gereksinimleri İndirilmesi
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 5) Sistem Başlangıcında Docker'ın Otomatik Açılması
```
sudo systemctl enable --now docker
```

### 6) Docker Versiyonunu Kontrol Edilmesi
```
docker --version
```
