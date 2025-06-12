class Estudiante:
    """Representa un estudiante de las Pruebas Aprender."""

    def __init__(self, provincia: str, puntaje_matematica: float, puntaje_lengua: float, puntaje_nse: float, ambito: str, sector: str) -> None:
        self.provincia = provincia
        self.puntaje_matematica = puntaje_matematica
        self.puntaje_lengua = puntaje_lengua
        self.puntaje_nse = puntaje_nse
        self.ambito = ambito
        self.sector = sector

    def __repr__(self) -> str:
        return f"<Mat:{self.puntaje_matematica:.2f}, Len:{self.puntaje_lengua:.2f}, NSE:{self.puntaje_nse:.2f}, {self.ambito.capitalize()}, {self.sector.capitalize()}, {self.provincia}>"

    def __eq__(self, other: "Estudiante") -> bool:
        return (
            isinstance(other, Estudiante) and
            self.provincia == other.provincia and
            abs(self.puntaje_matematica - other.puntaje_matematica) < 0.001 and
            abs(self.puntaje_lengua - other.puntaje_lengua) < 0.001 and
            abs(self.puntaje_nse - other.puntaje_nse) < 0.001 and
            self.ambito == other.ambito and
            self.sector == other.sector
        )