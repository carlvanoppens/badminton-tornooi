# Maakt index.html uit src/badminton-tornooi.html
import pathlib
here=pathlib.Path(__file__).parent
body=(here/'src'/'badminton-tornooi.html').read_text()
head='''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0e7a55">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Tornooi">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font-size:14px}img{max-width:100%}[hidden]{display:none!important}</style>
'''
tail='''
<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));</script>
</body>
</html>
'''
# <title>/<style>/<link> horen in de head; de rest (header, main, script) in de body
i=body.index('<header>')
out=head+body[:i]+'</head>\n<body>\n'+body[i:]+tail
(here/'index.html').write_text(out)
print('index.html', len(out), 'bytes')
