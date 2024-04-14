// NavegacionService.cs

using System;

public class NavegacionService {
    public bool Alumno { get; private set; }

    public event Action OnMostrarImagenChange;

    public void CambiarMostrarImagen(bool mostrar) {
        Alumno = mostrar;
        OnMostrarImagenChange?.Invoke();
    }
}
