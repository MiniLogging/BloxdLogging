"use strict";(self.webpackChunkbloxd=self.webpackChunkbloxd||[]).push([[42],{13310:(E,Y,C)=>{C.r(Y),C.d(Y,{rgbdEncodePixelShader:()=>u});var P=C(10827);C(11639);const K="rgbdEncodePixelShader",m="varying vec2 vUV;uniform sampler2D textureSampler;\n#include<helperFunctions>\n#define CUSTOM_FRAGMENT_DEFINITIONS\nvoid main(void) \n{gl_FragColor=toRGBD(texture2D(textureSampler,vUV).rgb);}";P.c.ShadersStore[K]=m;const u={name:K,shader:m}}}]);