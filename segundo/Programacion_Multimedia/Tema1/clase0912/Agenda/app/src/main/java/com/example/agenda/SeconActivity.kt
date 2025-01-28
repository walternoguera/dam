package com.example.agenda

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.agenda.databinding.ActivitySeconBinding

class SeconActivity : AppCompatActivity() {
    private lateinit var binding: ActivitySeconBinding
    private lateinit var correo: String
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySeconBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //recuperar los datos que me pasan
        correo = intent.getStringExtra("correo") ?: "No hay correo"
        binding.textoBienvenida.text = binding.textoBienvenida.text.toString() + " " + correo
    }
}