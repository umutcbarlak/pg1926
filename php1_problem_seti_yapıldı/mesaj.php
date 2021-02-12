<?php
$kullanici_adi = $_POST["kullanici_adi"];
$sifre = $_POST["sifre"];

if($kullanici_adi == "" or $sifre ==""){
    echo "<script>alert('Lütfen Bos alanları doldurunuz')</script>";
}
else{
    echo "<script>alert('Hosgeldin $kullanici_adi')</script>";
    date_default_timezone_set('Europe/Istanbul');
    $saat = date('H');
    if (($saat >=6) && ($saat <=10))
    {
    echo "Günaydın";
    }
    elseif (($saat >=10) && ($saat <=17))
    {
    echo "İyi Günler";
    }
    elseif (($saat >=17) && ($saat<=20))
    {
    echo "İyi Akşamlar";
    }
    elseif (($saat >=20) && ($saat<=24))
    {
    echo "İyi Geceler";
    }
    else
    {
    echo "Esenlikler Dilerim";
    }
    
}
?>