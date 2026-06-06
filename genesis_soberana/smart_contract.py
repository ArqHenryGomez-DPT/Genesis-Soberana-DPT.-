def ejecutar_smart_contract_biologico(ahorro_generado):
    pago_soberano = ahorro_generado * 0.15
    return {
        "60_Por_Ciento_Vida": pago_soberano * 0.60,
        "40_Por_Ciento_Estructura": pago_soberano * 0.40
    }
