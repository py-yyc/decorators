
# fuck all the things. rst2html5 Sucks All The Things and basically
# doesn't work. So, screw that. Lets try ... something else...

# my actual problem/issue was to directly inject Python into a slide
# template. So maybe lets do that directly...

from __future__ import print_function
import sys
import subprocess

from xml.sax.saxutils import escape

from pygments import highlight
from pygments.formatters import Terminal256Formatter, TerminalFormatter
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

preamble = open('preamble.html', 'r').read()
trailer = open('trailer.html', 'r').read()
#slide_template = open('one_slide.html', 'r').read()

slide_template = '''
  <div class="slide">
    {html}
    <div class="incremental">
      {code}
    </div>
  </div>
'''

def write_chunk(chunk, out):
    if not chunk.strip():
        return
    out.write(
        highlight(
            chunk, get_lexer_by_name('python'),
            formatter=formatter,
        )
    )
    out.write('<!--- chunk -->\n')

slides = sys.argv[1:]
out = open('slides.html', 'w')
out.write(preamble)
for slide in slides:
    lines = []
    with open(slide, 'r') as f:
        for line in f.readlines():
            if '# noslide' not in line:
                lines.append(line)
    formatter = HtmlFormatter(style='monokai')
    out.write('<div class="slide">\n')
    html = ''
    for line in lines:
        if line.strip().startswith('## '):
            if "show-output" not in line:
                html += line.strip()[3:]
    out.write('<!-- gathered html -->\n{}<!-- /html -->\n\n'.format(html))
    out.write('  <div class="incremental">\n')
    chunk = ''
    for line in lines:
        if line.strip().startswith('## '):
            continue
        if line.strip().startswith('#!'):
            write_chunk(chunk, out)
            chunk = ''
        else:
            chunk += line
    write_chunk(chunk, out)
    showoutput = False
    for line in lines:
        if "## show-output" in line:
            showoutput = True
            break
    if showoutput:
        output = subprocess.check_output(['python', slide])
        output = escape(output)
        out.write('<div class="output"><pre class="output">{}</pre></div>\n'.format(output))
    out.write('  </div>\n')  # ends "incremental code"
    out.write('</div>\n\n')  # ends slide

out.write(trailer)
out.close()
