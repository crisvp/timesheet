PREFIX=$(HOME)
PYINSTALLER=pyinstaller

all: dist/t

dist/t:
	$(PYINSTALLER) --hidden-import _strptime --additional-hooks-dir hooks -F t

install:
	install -d $(PREFIX)/bin
	install -m 0755 dist/t $(PREFIX)/bin/t

clean:
	rm dist/t

distclean:
	rm -r dist build
