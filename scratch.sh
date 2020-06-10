#!/bin/bash

function sendWhatsappMessage() {
  open -a WhatsApp https://wa.me/$1
 }
sendWhatsappMessage $1