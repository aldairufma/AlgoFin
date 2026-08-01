[app]
title = CodeFin Educacional
package.name = codefin
package.domain = br.com.aldair
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# REQUISITOS (Muito importante para a IA funcionar!)
requirements = python3, kivy==master, kivymd==1.2.0, requests, urllib3, charset-normalizer, idna, certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.archs = arm64-v8a