from app.db import SessionLocal
from app.main import app
from app.models import UserDB
from fastapi.testclient import TestClient
from sqlalchemy import insert, select

client = TestClient(app)


def _ensure_one_user() -> int | str:
    with SessionLocal() as db:
        row = db.execute(select(UserDB.id).limit(1)).first()
        if row:
            return row[0]
        ret = db.execute(
            insert(UserDB)
            .values(username="valentin", level=1, xp=0)
            .returning(UserDB.id)
        )
        db.commit()
        return ret.scalar_one()


def test_get_profile_200():
    uid = _ensure_one_user()
    r = client.get(f"/profiles/{uid}")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == uid
    assert "username" in data
    assert "xp" in data
    assert "level" in data


def test_update_me_200():
    _ensure_one_user()
    payload = {"username": "vali_new"}
    r = client.patch("/profiles/me", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["username"] == "vali_new"


def test_search_profiles_ok():
    _ensure_one_user()
    r = client.get("/profiles/search?q=val&page=1&page_size=10")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
