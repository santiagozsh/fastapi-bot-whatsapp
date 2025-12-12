
def extract_message_data (datajson: dict):
    """
    Recibe el JSON, lo procesa y devuelve los datos limpios
    """
    try:
        entry = datajson.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", [])
        messages = value.get("messages", [])
        # print("messages: ", messages)

        if not messages:
            None


        raw_message = messages[0]
        # print(raw_message)

        phone_number = raw_message.get("from")
        type_message = raw_message.get("type")
        timestamp = raw_message.get("timestamp")

        clean_data = {
            "text": None,
            "phone": phone_number,
            "timestamp": timestamp,
            "image_id": None,
            "raw_message": raw_message,
            "type": type_message
        }

        if type_message == "text":
            clean_data["text"] = raw_message["text"]["body"]
            # print(clean_data["text"])
        elif type_message == "image":
            image_data = raw_message["image"]
            clean_data["image_id"] = image_data.get("id")
            clean_data["text"] = image_data.get("caption")
            # print("imagedata: ", image_data)
            # print("text/caption:", clean_data["text"])
            # print("image+id", clean_data["image_id"])
        else: 
            print(f"Tipo de dato no soportado: {type_message}")
            return None

        print(clean_data)

        return clean_data

    except Exception as error:
        print(f"Error extrayendo datos: {error}")
