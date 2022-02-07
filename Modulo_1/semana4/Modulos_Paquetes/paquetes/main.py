import sound.effects.echo
from sound.effects import echo
from sound.effects.echo import echofilter
output = "output"
input = "input"

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
echo.echofilter(input, output, delay=0.7, atten=4)
echofilter(input, output, delay=0.7, atten=4)
