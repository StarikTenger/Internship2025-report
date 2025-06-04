from pylatexenc.latexencode import UnicodeToLatexEncoder
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python unicode-to-latex.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    encoder = UnicodeToLatexEncoder(non_ascii_only=True)
    latex_content = encoder.unicode_to_latex(content)

    # Overwrite the original file with the LaTeX-encoded content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(latex_content)

if __name__ == "__main__":
    main()
