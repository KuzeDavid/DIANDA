// NavegacionService.cs

using System;

public class NavegacionService {
    public bool MostrarImagen { get; private set; }

    public event Action OnMostrarImagenChange;

    public void CambiarMostrarImagen(bool mostrar) {
        MostrarImagen = mostrar;
        OnMostrarImagenChange?.Invoke();
    }
}
