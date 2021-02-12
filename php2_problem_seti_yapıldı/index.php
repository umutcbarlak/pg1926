<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>www.umutcemalbarlak.com</title>
<link rel="stylesheet" href="deneme.css">
</head>
<body>
    <h1>PHP Problem Seti 2 Ödevi</h1>
    <h2>umutcemalbarlak Saygıyla Sunarr...</h2>
        <form name="toplam" autocomplete="off">
            <label>Sayı : </label>
            <input type="text" id="txtSayi"><br><br>
            <input type="button" id="btnHesap" value="HESAPLA"><br><br>
            <label id="lblSonuc"></label>
        </form>
                    
<script>

    var btn=document.getElementById("btnHesap");
    btn.onclick=function(){
        var i,j;
        var toplam=0;
        var sayi=Number(document.getElementById("txtSayi").value);
        for(i=1;i<sayi;i++)
         {
             if (sayi%i==0)
             {
                toplam=toplam+i;	
             }
         }
             if (sayi==toplam)
             {
                
                alert(document.getElementById("lblSonuc").innerHTML=sayi + " Sayısı Mükemmel Sayıdır");	 
             }
             else
             {
                alert(document.getElementById("lblSonuc").innerHTML=sayi + " Sayısı Mükemmel Sayı Değildir");
             }
         }
</script>
</body>
</html>
