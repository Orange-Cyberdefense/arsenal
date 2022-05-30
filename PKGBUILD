#Maintainer: Viking @Vikingfr <https://twitter.com/Vikingfr>
#Maintainer: Mayfly @M4yFly <https://twitter.com/M4yFly>
#Maintainer: Erick Sanchez Vera "T1erno" <erickdeveloper2000@outlook com>

pkgname=arsenal
pkgver=1.1.0
pkgrel=1
pkgdesc='Arsenal is just a quick inventory and launcher for hacking programs'
url='https://github.com/Orange-Cyberdefense/arsenal'
arch=('any')
license=('GPL')
depends=('python>=3.7')
source=(${pkgname}::git+https://github.com/Orange-Cyberdefense/arsenal.git)
sha512sums=('SKIP')

build() {
	cd $pkgname
	python setup.py build
}

package() {
	cd $pkgname
	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
	install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
	install -Dm 644 README.md -t "${pkgdir}"/usr/share/doc/${pkgname}
}
