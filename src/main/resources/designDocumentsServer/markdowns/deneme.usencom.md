<div class="title">

# Kullanım Senaryosu: 
Deneme
</div>

<div style="padding:10px;margin:10px">

``` plantuml
actor User
User -> (Giriş/Yetki Kontrolü)
```

### Şekil 1: Kullanım Senaryosu Diagramı

</div>

<div style="padding:10px;margin:10px">
**Özet:**Deneme

**Fail:**Arşiv Görevlisi

**Ön Şart:**Deneme

**Ana Silsile:** Deneme

**Alternatif Silsile:**Deneme

**Beklenen Sonuç:**Giriş

</div>
<div style="padding:10px;margin:10px">
``` plantuml
allow_mixing
actor User 
object deneme <<user interface>> {
}
User - deneme : M1->
```
### Şekil 2: İletişim Diagramı

</div>

