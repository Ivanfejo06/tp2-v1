class Resumen:
    """Contiene estadísticas agregadas sobre un conjunto de estudiantes."""

    def __init__(self, cantidad: int, promedio_matematica: float, promedio_lengua: float, promedio_nse: float,
                 proporcion_ambito_rural: float, proporcion_sector_estatal: float) -> None:
        self.cantidad = cantidad
        self.promedio_matematica = promedio_matematica
        self.promedio_lengua = promedio_lengua
        self.promedio_nse = promedio_nse
        self.proporcion_ambito_rural = proporcion_ambito_rural
        self.proporcion_sector_estatal = proporcion_sector_estatal

    def __repr__(self) -> str:
        return f"<Mat:{self.promedio_matematica:.2f}, Len:{self.promedio_lengua:.2f}, NSE:{self.promedio_nse:.2f}, Rural:{self.proporcion_ambito_rural:.2f}, Estado:{self.proporcion_sector_estatal:.2f}, N:{self.cantidad}>"

    def __eq__(self, other: "Resumen") -> bool:
        return (
            isinstance(other, Resumen) and
            self.cantidad == other.cantidad and
            abs(self.promedio_matematica - other.promedio_matematica) < 0.001 and
            abs(self.promedio_lengua - other.promedio_lengua) < 0.001 and
            abs(self.promedio_nse - other.promedio_nse) < 0.001 and
            abs(self.proporcion_ambito_rural - other.proporcion_ambito_rural) < 0.001 and
            abs(self.proporcion_sector_estatal - other.proporcion_sector_estatal) < 0.001
        )
