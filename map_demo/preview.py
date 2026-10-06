from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def render_preview(payload: dict, destination: Path) -> Path:
    canvas = Image.new("RGB", (1320, 720), "#f2f5f3")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    draw.rounded_rectangle((42, 36, 1278, 676), radius=4, fill="#ffffff", outline="#cbd6d1")
    draw.rectangle((42, 36, 1278, 102), fill="#244f43")
    draw.text((660, 68), "SYNTHETIC EXPENSE MAP", anchor="mm", fill="#ffffff", font=font)
    draw.text((74, 130), f"Unit: {payload['unit']['name']}", fill="#244f43", font=font)
    draw.text((74, 154), f"Code: {payload['unit']['code']}     Period: {payload['period']}", fill="#596a63", font=font)
    columns = ((74, "#"), (122, "DOCUMENT"), (330, "SUPPLIER"), (655, "ISSUE DATE"), (790, "CATEGORY"), (1095, "AMOUNT"))
    draw.rectangle((62, 198, 1258, 238), fill="#ddebe5")
    for x, label in columns:
        draw.text((x, 213), label, fill="#244f43", font=font)
    y = 252
    total = 0
    for index, item in enumerate(payload["documents"], start=1):
        total += float(item["amount"])
        values = (str(index), item["reference"], item["supplier"], item["issued_on"], item["category"], f"$ {item['amount']:,.2f}")
        for (x, _), value in zip(columns, values, strict=True):
            draw.text((x, y), value, fill="#26352f", font=font)
        draw.line((62, y + 25, 1258, y + 25), fill="#e4e9e7")
        y += 48
    draw.rectangle((62, y, 1258, y + 46), fill="#edf4f1")
    draw.text((1030, y + 18), "TOTAL", fill="#244f43", font=font)
    draw.text((1095, y + 18), f"$ {total:,.2f}", fill="#244f43", font=font)
    draw.text((74, 638), "Generated from fictional JSON input · workbook includes validation sheet and dynamic formulas", fill="#66766f", font=font)
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, optimize=True)
    return destination
