import android.media.AudioManager
import android.media.ToneGenerator
import java.util.*

fun main() {
    val bpm = 120 // Beats por minuto
    val duration = 100 // Duración del tono en milisegundos
    val tone = ToneGenerator.TONE_CDMA_PIP // Tono a reproducir

    val metronome = Metronome(bpm, duration, tone)
    metronome.start()
}

class Metronome(private val bpm: Int, private val duration: Int, private val tone: Int) {
    private val timer = Timer()

    fun start() {
        val interval = 60000L / bpm // Calcula el intervalo de tiempo en milisegundos para el tempo dado
        timer.scheduleAtFixedRate(TimerTask { playTone() }, 0, interval)
    }

    private fun playTone() {
        val toneGenerator = ToneGenerator(AudioManager.STREAM_MUSIC, 100)
        toneGenerator.startTone(tone, duration)
    }
}

// probando comentarios para saber si actividad solo se cuenta en Branch main
