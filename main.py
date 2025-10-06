import sys
import os

def main():
    # Si se quiere probar comportamiento de fallo: export FAIL_HELLO=true
    # o ejecutar con argumento --fail
    if os.getenv("FAIL_HELLO", "").lower() == "true" or "--fail" in sys.argv:
        print("Simulando fallo en el job 'hello'", file=sys.stderr)
        sys.exit(1)
    print("Job 'hello' completado correctamente")

if __name__ == "__main__":
    main()
