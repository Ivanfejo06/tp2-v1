import csv
from typing import List, Set, Dict
from estudiante import Estudiante
from resumen import Resumen


class Pais:
    """Representa el conjunto de estudiantes de un país."""

    def __init__(self, archivo_csv: str) -> None:
        self.estudiantes: List[Estudiante] = []

        f = open(archivo_csv, encoding="utf-8")
        for fila in csv.DictReader(f):
            provincia = fila["provincia"]
            puntaje_mat = float(fila["mpuntaje"])
            puntaje_len = float(fila["lpuntaje"])
            puntaje_nse = float(fila["NSE_puntaje"])
            ambito = fila["ambito"]
            sector = fila["sector"]
            estudiante = Estudiante(provincia, puntaje_mat, puntaje_len, puntaje_nse, ambito, sector)
            self.estudiantes.append(estudiante)
        f.close()

        self._tamano = len(self.estudiantes)
        self.provincias: Set[str] = set(e.provincia for e in self.estudiantes)

    def tamano(self) -> int:
        return self._tamano

    def resumen_provincia(self, provincia: str) -> Resumen:
        filtrados = [e for e in self.estudiantes if e.provincia == provincia]
        n = len(filtrados)
        return Resumen(
            cantidad=n,
            promedio_matematica=sum(e.puntaje_matematica for e in filtrados) / n,
            promedio_lengua=sum(e.puntaje_lengua for e in filtrados) / n,
            promedio_nse=sum(e.puntaje_nse for e in filtrados) / n,
            proporcion_ambito_rural=sum(1 for e in filtrados if e.ambito == "rural") / n,
            proporcion_sector_estatal=sum(1 for e in filtrados if e.sector == "estatal") / n
        )

    def resumenes_pais(self) -> Dict[str, Resumen]:
        return {prov: self.resumen_provincia(prov) for prov in self.provincias}

    def estudiantes_en_intervalo(self, categoria: str, x: float, y: float, provincias: Set[str]) -> int:
        key_map = {"mat": "puntaje_matematica", "len": "puntaje_lengua", "nse": "puntaje_nse"}
        assert categoria in key_map
        return sum(
            1 for e in self.estudiantes
            if e.provincia in provincias and x <= getattr(e, key_map[categoria]) < y
        )

    def exportar_por_provincias(self, archivo_csv: str, provincias: Set[str]) -> None:
        campos = [
            "provincia", "cantidad", "promedio_matematica", "promedio_lengua", "promedio_nse",
            "proporcion_ambito_rural", "proporcion_sector_estatal"
        ]
        with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for prov in provincias:
                r = self.resumen_provincia(prov)
                writer.writerow({
                    "provincia": prov,
                    "cantidad": r.cantidad,
                    "promedio_matematica": f"{r.promedio_matematica:.2f}",
                    "promedio_lengua": f"{r.promedio_lengua:.2f}",
                    "promedio_nse": f"{r.promedio_nse:.2f}",
                    "proporcion_ambito_rural": f"{r.proporcion_ambito_rural:.2f}",
                    "proporcion_sector_estatal": f"{r.proporcion_sector_estatal:.2f}"
                })
