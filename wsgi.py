from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    #    return "Hello World!!!"
    response_body = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Welcome to OpenShift</title>
<style>
body{
  margin:0;
  font: 400 18px/1.3 Georgia,"Times New Roman",Times,"Kai","Kaiti SC","KaiTi","BiauKai","楷体","楷体_GB2312",serif;
  background-color:#f4f4ee;
}
article{
  position: absolute;
  top: 50%;
  left: 50%;
  width: 880px;
  height:520px;
  margin-top: -280px;
  margin-left: -410px;
  box-sizing:border-box;
  -moz-box-sizing:border-box; /* Firefox */
  -webkit-box-sizing:border-box; /* Safari */
  background:#fff;
  padding:20px 0;
  font-size:24px;
  -webkit-writing-mode: vertical-rl; /* for browsers of webkit engine */
  writing-mode: tb-rl; /* for ie old*/
  -ms-writing-mode: vertical-rl;
  box-shadow:5px 5px 15px rgba(0,0,0,.1)
}
article header{
  overflow:hidden;
  margin:0 30px 0 20px;
}
article h1{
  font-family:wt064;
  float:left;
  font-size: 48px;
}
article h2{
  float:left;
  color:#d32913;
  font-size:16px;
  margin:10px 20px 0 0;
}
article p{
  word-spacing:.5em;
}
</style>
</head>
<body>
<div style="float:left;margin:2em">
 var monthNames = [
    "01", "02", "03",
    "04", "05", "06", "07",
    "08", "09", "10",
    "11", "12"
  ];
var local = new Date();
local.setHours(local.getHours()-7);
document.write(local.getFullYear(), monthNames[local.getMonth()], ('000'+local.getDate()).substr(-2))</script></a>
<br>
<script>document.write(new Date())</script>
</div>
<article>
  <header>
    <h1>蘭亭集序</h1>
    <h2>王羲之 晉代</h2>
  </header>
  <div id="content" class="content">
    <p class="">永和九年歲在癸醜暮春之初會於會稽山陰之蘭亭修禊事也群賢畢至少長鹹集此地有崇山峻嶺茂林修竹又有清流激湍映帶左右引以為流觴曲水列坐其次雖無絲竹管絃之盛，一觴一詠亦足以暢敘幽情</p>
    <p>是日也天朗氣清惠風和暢仰觀宇宙之大俯察品類之盛所以遊目騁懷足以極視聽之娛信可樂也</p>
    <p>夫人之相與俯仰一世或取諸懷抱晤言一室之內或因寄所託放浪形骸之外雖趣舍萬殊靜躁不同當其欣於所遇暫得於己快然自足不知老之將至及其所之既倦情隨事遷感慨係之矣向之所欣俛仰之間已為陳跡猶不能不以之興懷況修短隨化終期於盡古人雲死生亦大矣豈不痛哉</p>
    <p>每覽昔人興感之由若合一契未嘗不臨文嗟悼不能喻之於懷固知一死生為虛誕齊彭殤為妄作後之視今亦猶今之視昔悲夫故列敘時人錄其所述雖世殊事異所以興懷其致一也後之覽者亦將有感於斯文</p>
  </div>
</article>
<script>
var tts = function() {
    a = document.createElement('a');
    a.id = 'tts';
    a.innerText = '  ' + String.fromCharCode(55357, 56803);
    document.getElementsByTagName('h1')[0].appendChild(a);
    document.getElementById('tts').addEventListener('click', speak);
}
function p(){
    speechSynthesis.pause();
    document.getElementById('tts').removeEventListener('click', p);
    document.getElementById('tts').addEventListener('click', r);
}
function r(){
    speechSynthesis.resume();
    document.getElementById('tts').removeEventListener('click', r);
    document.getElementById('tts').addEventListener('click', p);
}
function speak(text, callback) {
    text = document.getElementById('content').innerText;
    text = text.replace(String.fromCharCode(55357, 56803),'');
    text = text.replace(String.fromCharCode(12290), '');
    dialogue = text.split(String.fromCharCode(12300));
    var x = new SpeechSynthesisUtterance(dialogue);
    x.lang = 'zh-HK';
    x.pitch = 0.8 ;
    x.rate = 0.8 ;
    speechSynthesis.cancel();
    speechSynthesis.speak(x);
    emoji = String.fromCharCode(9199);
    document.getElementById('tts').innerHTML =  '  ' + emoji;
    document.getElementById('tts').removeEventListener('click', speak);
    document.getElementById('tts').addEventListener('click', p);
}
document.addEventListener("DOMContentLoaded", tts);
</script>
</body></html>
'''
    status = '200 OK'
    response_headers = [('Content-Type', ctype),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

if __name__ == "__main__":
    application.run()
