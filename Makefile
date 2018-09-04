PREFIX=$(HOME)
PYINSTALLER=pyinstaller

all: dist/t

dist/t:
	$(PYINSTALLER) --hidden-import _strptime --additional-hooks-dir hooks -F t

install: dist/t
	install -d $(PREFIX)/bin
	install -m 0755 dist/t $(PREFIX)/bin/t

clean:
	rm -f dist/t

distclean: clean
	rm -rf dist build *.spec
