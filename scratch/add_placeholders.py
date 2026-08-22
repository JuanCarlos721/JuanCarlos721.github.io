import re

html_path = r'C:\Users\Juan Carlos\Downloads\UNI\3er cuatri\Estructuras de Datos y Algoritmos\JuanCarlos721.github.io\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

placeholders = """</pre>
            </div>
            
            <div class="queque-placeholder">
                <p>Mejor Caso: <span>QUEQUE</span></p>
            </div>
            <div class="queque-placeholder">
                <p>Caso Promedio: <span>QUEQUE</span></p>
            </div>
            <div class="queque-placeholder">
                <p>Peor Caso: <span>QUEQUE</span></p>
            </div>
        </div>"""

# Replace the end of each meta section
new_content = re.sub(r'</pre>\s*</div>\s*</div>', placeholders, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Replaced", len(re.findall(r'</pre>\s*</div>\s*</div>', content)), "meta sections.")
