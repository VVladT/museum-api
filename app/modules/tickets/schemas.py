#TicketResponse { // Se devuelven varios de una compra
#  fecha: Date,
#  visitante: VisitanteResponse,
#  tipoTicket: TipoTicketResponse, // (Mayor de edad, menor de edad, estudiante universitario o tecnico),
#  comprador: VisitanteResponse // Es quien compra, no necesariamente el visitante que irá, puede ser un familiar.
#}
#
#TicketRequest {
#  id: number,
#  fecha: string, // (Usar formato ISO YYYY-MM-DD)
#  visitantes: VisitanteRequest[],
#  comprador:
#}
