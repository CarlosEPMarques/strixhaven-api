# Data Model

## Enumerations

### `user_role`

* Possible values: `'DM'`, `'PLAYER'`

### `news_category`

* Possible values: `'EVENT'`, `'ANNOUNCEMENT'`, `'UPDATE'`, `'OTHER'`

### `calendar_event_type`

* Possible values: `'CLASS'`, `'EXAM'`, `'HOLIDAY'`, `'OTHER'`

### `store_item_rarity`

* Possible values: `'COMMON'`, `'UNCOMMON'`, `'RARE'`, `'EPIC'`, `'LEGENDARY'`

### `npc_occupation`

* Possible values: `'PROFESSOR'`, `'STUDENT'`, `'MERCHANT'`, `'OTHER'`

---

## Tables

### `users`

| Column       | Type         | Constraints      | Description                |
| ------------ | ------------ | ---------------- | -------------------------- |
| id           | BIGSERIAL    | PK               | Internal identifier        |
| external\_id | UUID         | UNIQUE           | External identifier        |
| name         | VARCHAR(100) | NOT NULL         | User's name                |
| email        | VARCHAR(100) | UNIQUE, NOT NULL | User's email               |
| password     | VARCHAR(255) | NOT NULL         | User's password            |
| role         | `user_role`  | NOT NULL         | User's role                |
| avatar\_url  | TEXT         |                  | URL to user's avatar image |
| created\_at  | TIMESTAMP    | DEFAULT NOW()    | Creation timestamp         |
| updated\_at  | TIMESTAMP    | DEFAULT NOW()    | Update timestamp           |

---

### `colleges`

| Column        | Type         | Constraints   | Description          |
| ------------- | ------------ | ------------- | -------------------- |
| id            | BIGSERIAL    | PK            | Internal identifier  |
| external\_id  | UUID         | UNIQUE        | External identifier  |
| name          | VARCHAR(100) | NOT NULL      | College name         |
| description   | TEXT         |               | College description  |
| image\_url    | TEXT         |               | URL to college image |
| founded\_year | INT          |               | Year founded         |
| traditions    | JSONB        |               | College traditions   |
| created\_at   | TIMESTAMP    | DEFAULT NOW() | Creation timestamp   |
| updated\_at   | TIMESTAMP    | DEFAULT NOW() | Update timestamp     |

---

### `books`

| Column       | Type         | Constraints   | Description         |
| ------------ | ------------ | ------------- | ------------------- |
| id           | BIGSERIAL    | PK            | Internal identifier |
| external\_id | UUID         | UNIQUE        | External identifier |
| title        | VARCHAR(100) | NOT NULL      | Book title          |
| summary      | TEXT         |               | Book summary        |
| section      | VARCHAR(100) |               | Book section        |
| language     | VARCHAR(50)  |               | Book language       |
| is\_hidden   | BOOLEAN      | DEFAULT FALSE | Visibility flag     |
| image\_url   | TEXT         |               | Book image URL      |
| created\_at  | TIMESTAMP    | DEFAULT NOW() | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW() | Update timestamp    |

---

### `maps`

| Column       | Type         | Constraints | Description         |
| ------------ | ------------ | ----------- | ------------------- |
| id           | BIGSERIAL    | PK          | Internal identifier |
| external\_id | UUID         | UNIQUE      | External identifier |
| title        | VARCHAR(100) | NOT NULL    | Map title           |
| image\_url   | TEXT         |             | Map image URL       |

---

### `monsters`

| Column             | Type         | Constraints   | Description         |
| ------------------ | ------------ | ------------- | ------------------- |
| id                 | BIGSERIAL    | PK            | Internal identifier |
| external\_id       | UUID         | UNIQUE        | External identifier |
| name               | VARCHAR(100) | NOT NULL      | Monster name        |
| size               | VARCHAR(50)  |               | Monster size        |
| alignment          | VARCHAR(50)  |               | Alignment           |
| armor\_class       | INT          |               | Armor Class         |
| hit\_points        | INT          |               | Hit Points          |
| speed              | VARCHAR(50)  |               | Movement speed      |
| abilities          | JSONB        |               | Monster abilities   |
| actions            | JSONB        |               | Monster actions     |
| experience\_points | INT          |               | Experience points   |
| strength           | INT          |               | Strength            |
| dexterity          | INT          |               | Dexterity           |
| constitution       | INT          |               | Constitution        |
| intelligence       | INT          |               | Intelligence        |
| wisdom             | INT          |               | Wisdom              |
| charisma           | INT          |               | Charisma            |
| description        | TEXT         |               | Monster description |
| image\_url         | TEXT         |               | Monster image URL   |
| created\_at        | TIMESTAMP    | DEFAULT NOW() | Creation timestamp  |
| updated\_at        | TIMESTAMP    | DEFAULT NOW() | Update timestamp    |

---

### `news`

| Column         | Type            | Constraints   | Description         |
| -------------- | --------------- | ------------- | ------------------- |
| id             | BIGSERIAL       | PK            | Internal identifier |
| external\_id   | UUID            | UNIQUE        | External identifier |
| headline       | VARCHAR(100)    | NOT NULL      | News headline       |
| body           | TEXT            |               | News body           |
| category       | `news_category` |               | News category       |
| game\_datetime | TIMESTAMP       |               | In-game date/time   |
| image\_url     | TEXT            |               | News image URL      |
| created\_at    | TIMESTAMP       | DEFAULT NOW() | Creation timestamp  |
| updated\_at    | TIMESTAMP       | DEFAULT NOW() | Update timestamp    |

---

### `stores`

| Column       | Type         | Constraints   | Description         |
| ------------ | ------------ | ------------- | ------------------- |
| id           | BIGSERIAL    | PK            | Internal identifier |
| external\_id | UUID         | UNIQUE        | External identifier |
| name         | VARCHAR(100) | NOT NULL      | Store name          |
| location     | VARCHAR(100) |               | Store location      |
| description  | TEXT         |               | Store description   |
| image\_url   | TEXT         |               | Store image URL     |
| created\_at  | TIMESTAMP    | DEFAULT NOW() | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW() | Update timestamp    |

---

### `calendar_events`

| Column         | Type                  | Constraints   | Description         |
| -------------- | --------------------- | ------------- | ------------------- |
| id             | BIGSERIAL             | PK            | Internal identifier |
| external\_id   | UUID                  | UNIQUE        | External identifier |
| title          | VARCHAR(100)          | NOT NULL      | Event title         |
| description    | TEXT                  |               | Event description   |
| game\_datetime | TIMESTAMP             |               | In-game date/time   |
| is\_exam       | BOOLEAN               | DEFAULT FALSE | Exam flag           |
| event\_type    | `calendar_event_type` |               | Type of event       |
| created\_at    | TIMESTAMP             | DEFAULT NOW() | Creation timestamp  |
| updated\_at    | TIMESTAMP             | DEFAULT NOW() | Update timestamp    |

---

### `npcs`

| Column        | Type             | Constraints                             | Description         |
| ------------- | ---------------- | --------------------------------------- | ------------------- |
| id            | BIGSERIAL        | PK                                      | Internal identifier |
| external\_id  | UUID             | UNIQUE                                  | External identifier |
| name          | VARCHAR(100)     | NOT NULL                                | NPC name            |
| college\_id   | BIGSERIAL        | FK to `colleges(id)` ON DELETE SET NULL | NPC's college       |
| college\_year | INT              |                                         | NPC's college year  |
| image\_url    | TEXT             |                                         | NPC image URL       |
| bio           | TEXT             |                                         | NPC biography       |
| occupation    | `npc_occupation` |                                         | NPC occupation      |
| personality   | JSONB            |                                         | NPC personality     |
| location      | VARCHAR(100)     |                                         | NPC location        |
| is\_visible   | BOOLEAN          | DEFAULT TRUE                            | Visibility flag     |
| created\_at   | TIMESTAMP        | DEFAULT NOW()                           | Creation timestamp  |
| updated\_at   | TIMESTAMP        | DEFAULT NOW()                           | Update timestamp    |

---

### `player_characters`

| Column        | Type         | Constraints                             | Description         |
| ------------- | ------------ | --------------------------------------- | ------------------- |
| id            | BIGSERIAL    | PK                                      | Internal identifier |
| external\_id  | UUID         | UNIQUE                                  | External identifier |
| user\_id      | BIGSERIAL    | FK to `users(id)` ON DELETE CASCADE     | Owning user         |
| name          | VARCHAR(100) | NOT NULL                                | Character name      |
| image\_url    | TEXT         |                                         | Character image URL |
| college\_year | INT          |                                         | College year        |
| college\_id   | BIGSERIAL    | FK to `colleges(id)` ON DELETE SET NULL | Character's college |
| level         | INT          |                                         | Character level     |
| goals         | TEXT         |                                         | Character goals     |
| hobbies       | JSONB        |                                         | Character hobbies   |
| allies        | JSONB        |                                         | Allies              |
| enemies       | JSONB        |                                         | Enemies             |
| created\_at   | TIMESTAMP    | DEFAULT NOW()                           | Creation timestamp  |
| updated\_at   | TIMESTAMP    | DEFAULT NOW()                           | Update timestamp    |

---

### `classes`

| Column       | Type         | Constraints                             | Description         |
| ------------ | ------------ | --------------------------------------- | ------------------- |
| id           | BIGSERIAL    | PK                                      | Internal identifier |
| external\_id | UUID         | UNIQUE                                  | External identifier |
| name         | VARCHAR(100) | NOT NULL                                | Class name          |
| description  | TEXT         |                                         | Class description   |
| college\_id  | BIGSERIAL    | FK to `colleges(id)` ON DELETE SET NULL | Associated college  |
| image\_url   | TEXT         |                                         | Class image URL     |
| created\_at  | TIMESTAMP    | DEFAULT NOW()                           | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW()                           | Update timestamp    |

---

### `class_professors`

| Column       | Type      | Constraints                           | Description         |
| ------------ | --------- | ------------------------------------- | ------------------- |
| id           | BIGSERIAL | PK                                    | Internal identifier |
| external\_id | UUID      | UNIQUE                                | External identifier |
| class\_id    | BIGSERIAL | FK to `classes(id)` ON DELETE CASCADE | Associated class    |
| npc\_id      | BIGSERIAL | FK to `npcs(id)` ON DELETE CASCADE    | Professor NPC       |

---

### `grades`

| Column        | Type      | Constraints                                     | Description         |
| ------------- | --------- | ----------------------------------------------- | ------------------- |
| id            | BIGSERIAL | PK                                              | Internal identifier |
| external\_id  | UUID      | UNIQUE                                          | External identifier |
| character\_id | BIGSERIAL | FK to `player_characters(id)` ON DELETE CASCADE | Character graded    |
| class\_id     | BIGSERIAL | FK to `classes(id)` ON DELETE CASCADE           | Related class       |
| score         | INT       |                                                 | Numeric score       |
| created\_at   | TIMESTAMP | DEFAULT NOW()                                   | Creation timestamp  |
| updated\_at   | TIMESTAMP | DEFAULT NOW()                                   | Update timestamp    |

**Unique:** (character\_id, class\_id)

---

### `quests`

| Column           | Type         | Constraints                         | Description         |
| ---------------- | ------------ | ----------------------------------- | ------------------- |
| id               | BIGSERIAL    | PK                                  | Internal identifier |
| external\_id     | UUID         | UNIQUE                              | External identifier |
| title            | VARCHAR(150) | NOT NULL                            | Quest title         |
| description      | TEXT         |                                     | Quest description   |
| responsible\_npc | BIGSERIAL    | FK to `npcs(id)` ON DELETE SET NULL | NPC responsible     |
| active           | BOOLEAN      | DEFAULT TRUE                        | Active flag         |
| rewards          | JSONB        |                                     | Rewards metadata    |
| expire\_date     | TIMESTAMP    |                                     | Expiration date     |
| created\_at      | TIMESTAMP    | DEFAULT NOW()                       | Creation timestamp  |
| updated\_at      | TIMESTAMP    | DEFAULT NOW()                       | Update timestamp    |

---

### `store_items`

| Column       | Type                | Constraints                          | Description         |
| ------------ | ------------------- | ------------------------------------ | ------------------- |
| id           | BIGSERIAL           | PK                                   | Internal identifier |
| external\_id | UUID                | UNIQUE                               | External identifier |
| store\_id    | BIGSERIAL           | FK to `stores(id)` ON DELETE CASCADE | Owning store        |
| name         | VARCHAR(100)        | NOT NULL                             | Item name           |
| description  | TEXT                |                                      | Item description    |
| price        | DECIMAL(10,2)       |                                      | Price               |
| rarity       | `store_item_rarity` |                                      | Item rarity         |
| durability   | INT                 |                                      | Durability/uses     |
| lore         | TEXT                |                                      | Item lore/flavor    |
| image\_url   | TEXT                |                                      | Item image URL      |
| created\_at  | TIMESTAMP           | DEFAULT NOW()                        | Creation timestamp  |
| updated\_at  | TIMESTAMP           | DEFAULT NOW()                        | Update timestamp    |

---

### `item_identifications`

| Column         | Type      | Constraints                                      | Description                |
| -------------- | --------- | ------------------------------------------------ | -------------------------- |
| id             | BIGSERIAL | PK                                               | Internal identifier        |
| external\_id   | UUID      | UNIQUE                                           | External identifier        |
| item\_id       | BIGSERIAL | FK to `store_items(id)` ON DELETE CASCADE        | Identified item            |
| character\_id  | BIGSERIAL | FK to `player_characters(id)` ON DELETE SET NULL | Discovering character      |
| discovered\_at | TIMESTAMP | DEFAULT NOW()                                    | Discovery timestamp        |
| notes          | TEXT      |                                                  | Notes about identification |

---

### `character_sheet`

| Column               | Type      | Constraints                                             | Description             |
| -------------------- | --------- | ------------------------------------------------------- | ----------------------- |
| id                   | BIGSERIAL | PK                                                      | Internal identifier     |
| external\_id         | UUID      | UNIQUE                                                  | External identifier     |
| character\_id        | BIGSERIAL | UNIQUE, FK to `player_characters(id)` ON DELETE CASCADE | Related character       |
| strength             | INTEGER   |                                                         | STR                     |
| dexterity            | INTEGER   |                                                         | DEX                     |
| constitution         | INTEGER   |                                                         | CON                     |
| intelligence         | INTEGER   |                                                         | INT                     |
| wisdom               | INTEGER   |                                                         | WIS                     |
| charisma             | INTEGER   |                                                         | CHA                     |
| proficiency\_bonus   | INTEGER   |                                                         | Proficiency bonus       |
| armor\_class         | INTEGER   |                                                         | Armor Class             |
| initiative           | INTEGER   |                                                         | Initiative              |
| speed                | INTEGER   |                                                         | Speed                   |
| max\_hit\_points     | INTEGER   |                                                         | Max HP                  |
| current\_hit\_points | INTEGER   |                                                         | Current HP              |
| temp\_hit\_points    | INTEGER   |                                                         | Temporary HP            |
| hit\_dice\_total     | INTEGER   |                                                         | Total hit dice          |
| hit\_dice\_current   | INTEGER   |                                                         | Current hit dice        |
| save\_str            | INTEGER   |                                                         | STR save                |
| save\_dex            | INTEGER   |                                                         | DEX save                |
| save\_con            | INTEGER   |                                                         | CON save                |
| save\_int            | INTEGER   |                                                         | INT save                |
| save\_wis            | INTEGER   |                                                         | WIS save                |
| save\_cha            | INTEGER   |                                                         | CHA save                |
| skills               | JSONB     |                                                         | Skill profs/bonuses     |
| background           | TEXT      |                                                         | Background              |
| race                 | TEXT      |                                                         | Race                    |
| alignment            | TEXT      |                                                         | Alignment               |
| experience\_points   | INTEGER   |                                                         | XP                      |
| languages            | JSONB     |                                                         | Known languages         |
| features\_traits     | JSONB     |                                                         | Features & traits       |
| proficiencies        | JSONB     |                                                         | Weapon/tool/armor profs |
| description          | TEXT      |                                                         | Free-form description   |
| created\_at          | TIMESTAMP | DEFAULT NOW()                                           | Creation timestamp      |
| updated\_at          | TIMESTAMP | DEFAULT NOW()                                           | Update timestamp        |

---

### `spells`

| Column       | Type         | Constraints   | Description            |
| ------------ | ------------ | ------------- | ---------------------- |
| id           | BIGSERIAL    | PK            | Internal identifier    |
| external\_id | UUID         | UNIQUE        | External identifier    |
| name         | VARCHAR(100) | NOT NULL      | Spell name             |
| level        | INT          |               | Spell level            |
| cast\_modes  | JSONB        |               | Casting modes/variants |
| description  | TEXT         |               | Spell description      |
| created\_at  | TIMESTAMP    | DEFAULT NOW() | Creation timestamp     |
| updated\_at  | TIMESTAMP    | DEFAULT NOW() | Update timestamp       |

---

### `stories`

| Column       | Type         | Constraints   | Description         |
| ------------ | ------------ | ------------- | ------------------- |
| id           | BIGSERIAL    | PK            | Internal identifier |
| external\_id | UUID         | UNIQUE        | External identifier |
| title        | VARCHAR(150) |               | Story title         |
| content      | TEXT         |               | Story content       |
| created\_at  | TIMESTAMP    | DEFAULT NOW() | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW() | Update timestamp    |

---

### `clubs`

| Column       | Type         | Constraints                            | Description         |
| ------------ | ------------ | -------------------------------------- | ------------------- |
| id           | BIGSERIAL    | PK                                     | Internal identifier |
| external\_id | UUID         | UNIQUE                                 | External identifier |
| name         | VARCHAR(100) | NOT NULL                               | Club name           |
| description  | TEXT         |                                        | Club description    |
| college\_id  | BIGSERIAL    | FK to `colleges(id)` ON DELETE CASCADE | College owner       |
| created\_at  | TIMESTAMP    | DEFAULT NOW()                          | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW()                          | Update timestamp    |

---

### `character_clubs`

| Column        | Type      | Constraints                                     | Description         |
| ------------- | --------- | ----------------------------------------------- | ------------------- |
| id            | BIGSERIAL | PK                                              | Internal identifier |
| external\_id  | UUID      | UNIQUE                                          | External identifier |
| character\_id | BIGSERIAL | FK to `player_characters(id)` ON DELETE CASCADE | Character member    |
| club\_id      | BIGSERIAL | FK to `clubs(id)` ON DELETE CASCADE             | Club                |

---

### `pets`

| Column       | Type         | Constraints                                     | Description         |
| ------------ | ------------ | ----------------------------------------------- | ------------------- |
| id           | BIGSERIAL    | PK                                              | Internal identifier |
| external\_id | UUID         | UNIQUE                                          | External identifier |
| owner\_id    | BIGSERIAL    | FK to `player_characters(id)` ON DELETE CASCADE | Owning character    |
| name         | VARCHAR(100) | NOT NULL                                        | Pet name            |
| species      | VARCHAR(100) |                                                 | Species             |
| description  | TEXT         |                                                 | Pet description     |
| abilities    | JSONB        |                                                 | Special abilities   |
| created\_at  | TIMESTAMP    | DEFAULT NOW()                                   | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW()                                   | Update timestamp    |

---

### `tournaments`

| Column       | Type         | Constraints   | Description         |
| ------------ | ------------ | ------------- | ------------------- |
| id           | BIGSERIAL    | PK            | Internal identifier |
| external\_id | UUID         | UNIQUE        | External identifier |
| title        | VARCHAR(100) | NOT NULL      | Tournament title    |
| description  | TEXT         |               | Description         |
| event\_date  | TIMESTAMP    |               | Event date/time     |
| created\_at  | TIMESTAMP    | DEFAULT NOW() | Creation timestamp  |
| updated\_at  | TIMESTAMP    | DEFAULT NOW() | Update timestamp    |

---

### `tournament_results`

| Column         | Type      | Constraints                                     | Description         |
| -------------- | --------- | ----------------------------------------------- | ------------------- |
| id             | BIGSERIAL | PK                                              | Internal identifier |
| external\_id   | UUID      | UNIQUE                                          | External identifier |
| tournament\_id | BIGSERIAL | FK to `tournaments(id)` ON DELETE CASCADE       | Tournament          |
| character\_id  | BIGSERIAL | FK to `player_characters(id)` ON DELETE CASCADE | Participant         |
| position       | INT       |                                                 | Final position      |
| reward         | JSONB     |                                                 | Reward metadata     |

---

### `student_scoreboard`

| Column           | Type         | Constraints   | Description            |
| ---------------- | ------------ | ------------- | ---------------------- |
| id               | BIGSERIAL    | PK            | Internal identifier    |
| external\_id     | UUID         | UNIQUE        | External identifier    |
| ranking          | INT          |               | Rank position          |
| student\_name    | VARCHAR(100) |               | Student name           |
| student\_college | VARCHAR(100) |               | Student college (text) |
| created\_at      | TIMESTAMP    | DEFAULT NOW() | Creation timestamp     |
| updated\_at      | TIMESTAMP    | DEFAULT NOW() | Update timestamp       |

---

### `inventory_items`

| Column        | Type      | Constraints                                     | Description           |
| ------------- | --------- | ----------------------------------------------- | --------------------- |
| id            | BIGSERIAL | PK                                              | Internal identifier   |
| external\_id  | UUID      | UNIQUE                                          | External identifier   |
| character\_id | BIGSERIAL | FK to `player_characters(id)` ON DELETE CASCADE | Owning character      |
| item\_id      | BIGSERIAL | FK to `store_items(id)` ON DELETE SET NULL      | Referenced store item |
| amount        | INT       |                                                 | Quantity              |
| metadata      | JSONB     |                                                 | Extra item metadata   |
| created\_at   | TIMESTAMP | DEFAULT NOW()                                   | Creation timestamp    |
| updated\_at   | TIMESTAMP | DEFAULT NOW()                                   | Update timestamp      |

**Unique:** (character\_id, item\_id)

---

### `npcs_reputation`

| Column        | Type      | Constraints                                     | Description         |
| ------------- | --------- | ----------------------------------------------- | ------------------- |
| id            | BIGSERIAL | PK                                              | Internal identifier |
| external\_id  | UUID      | UNIQUE                                          | External identifier |
| character\_id | BIGSERIAL | FK to `player_characters(id)` ON DELETE CASCADE | Character           |
| npc\_id       | BIGSERIAL | FK to `npcs(id)` ON DELETE CASCADE              | NPC                 |
| score         | INT       |                                                 | Reputation score    |
| created\_at   | TIMESTAMP | DEFAULT NOW()                                   | Creation timestamp  |
| updated\_at   | TIMESTAMP | DEFAULT NOW()                                   | Update timestamp    |

**Unique:** (character\_id, npc\_id)

---

### `notes`

| Column           | Type         | Constraints                         | Description             |
| ---------------- | ------------ | ----------------------------------- | ----------------------- |
| id               | BIGSERIAL    | PK                                  | Internal identifier     |
| external\_id     | UUID         | UNIQUE                              | External identifier     |
| author\_id       | BIGSERIAL    | FK to `users(id)` ON DELETE CASCADE | Author user             |
| title            | VARCHAR(150) |                                     | Note title              |
| content          | TEXT         | NOT NULL                            | Note content            |
| is\_master\_only | BOOLEAN      | DEFAULT FALSE                       | Visible to DM only flag |
| created\_at      | TIMESTAMP    | DEFAULT NOW()                       | Creation timestamp      |
| updated\_at      | TIMESTAMP    | DEFAULT NOW()                       | Update timestamp        |

---

### `character_notes`

| Column        | Type      | Constraints                                     | Description         |
| ------------- | --------- | ----------------------------------------------- | ------------------- |
| id            | BIGSERIAL | PK                                              | Internal identifier |
| external\_id  | UUID      | UNIQUE                                          | External identifier |
| note\_id      | BIGSERIAL | FK to `notes(id)` ON DELETE CASCADE             | Linked note         |
| character\_id | BIGSERIAL | FK to `player_characters(id)` ON DELETE CASCADE | Target character    |

---

### `npc_notes`

| Column       | Type      | Constraints                         | Description         |
| ------------ | --------- | ----------------------------------- | ------------------- |
| id           | BIGSERIAL | PK                                  | Internal identifier |
| external\_id | UUID      | UNIQUE                              | External identifier |
| note\_id     | BIGSERIAL | FK to `notes(id)` ON DELETE CASCADE | Linked note         |
| npc\_id      | BIGSERIAL | FK to `npcs(id)` ON DELETE CASCADE  | Target NPC          |
| author\_id   | BIGSERIAL | FK to `users(id)` ON DELETE CASCADE | Author user         |

---

### `npc_visibility`

| Column       | Type      | Constraints                         | Description                 |
| ------------ | --------- | ----------------------------------- | --------------------------- |
| id           | BIGSERIAL | PK                                  | Internal identifier         |
| external\_id | UUID      | UNIQUE                              | External identifier         |
| npc\_id      | BIGSERIAL | FK to `npcs(id)` ON DELETE CASCADE  | NPC                         |
| player\_id   | BIGSERIAL | FK to `users(id)` ON DELETE CASCADE | Player user with visibility |

---

### `character_classes`

| Column        | Type      | Constraints | Description         |
| ------------- | --------- | ----------- | ------------------- |
| id            | BIGSERIAL | PK          | Internal identifier |
| class\_id     | BIGSERIAL | FK          |                     |
| character\_id | BIGSERIAL | FK          |                     |

**Primary Key:** (character\_id, class\_id)

---

## Mermaid Diagram

```mermaid
erDiagram
    users {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        VARCHAR email UK
        VARCHAR password
        user_role role
        TEXT avatar_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    colleges {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        TEXT description
        TEXT image_url
        INT founded_year
        JSONB traditions
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    player_characters {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL user_id FK
        VARCHAR name
        TEXT image_url
        INT college_year
        BIGSERIAL college_id FK
        INT level
        TEXT goals
        JSONB hobbies
        JSONB allies
        JSONB enemies
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    npcs {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        BIGSERIAL college_id FK
        INT college_year
        TEXT image_url
        TEXT bio
        npc_occupation occupation
        JSONB personality
        VARCHAR location
        BOOLEAN is_visible
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    classes {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        TEXT description
        BIGSERIAL college_id FK
        TEXT image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    class_professors {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL class_id FK
        BIGSERIAL npc_id FK
    }

    grades {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL character_id FK
        BIGSERIAL class_id FK
        INT score
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    character_sheet {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL character_id FK
        INTEGER strength
        INTEGER dexterity
        INTEGER constitution
        INTEGER intelligence
        INTEGER wisdom
        INTEGER charisma
        INTEGER proficiency_bonus
        INTEGER armor_class
        INTEGER initiative
        INTEGER speed
        INTEGER max_hit_points
        INTEGER current_hit_points
        INTEGER temp_hit_points
        INTEGER hit_dice_total
        INTEGER hit_dice_current
        INTEGER save_str
        INTEGER save_dex
        INTEGER save_con
        INTEGER save_int
        INTEGER save_wis
        INTEGER save_cha
        JSONB skills
        TEXT background
        TEXT race
        TEXT alignment
        INTEGER experience_points
        JSONB languages
        JSONB features_traits
        JSONB proficiencies
        TEXT description
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    clubs {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        TEXT description
        BIGSERIAL college_id FK
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    character_clubs {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL character_id FK
        BIGSERIAL club_id FK
    }

    stores {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        VARCHAR location
        TEXT description
        TEXT image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    store_items {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL store_id FK
        VARCHAR name
        TEXT description
        DECIMAL price
        store_item_rarity rarity
        INT durability
        TEXT lore
        TEXT image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    inventory_items {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL character_id FK
        BIGSERIAL item_id FK
        INT amount
        JSONB metadata
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    item_identifications {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL item_id FK
        BIGSERIAL character_id FK
        TIMESTAMP discovered_at
        TEXT notes
    }

    quests {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR title
        TEXT description
        BIGSERIAL responsible_npc FK
        BOOLEAN active
        JSONB rewards
        TIMESTAMP expire_date
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    pets {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL owner_id FK
        VARCHAR name
        VARCHAR species
        TEXT description
        JSONB abilities
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    tournaments {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR title
        TEXT description
        TIMESTAMP event_date
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    tournament_results {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL tournament_id FK
        BIGSERIAL character_id FK
        INT position
        JSONB reward
    }

    npcs_reputation {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL character_id FK
        BIGSERIAL npc_id FK
        INT score
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    notes {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL author_id FK
        VARCHAR title
        TEXT content
        BOOLEAN is_master_only
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    character_notes {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL note_id FK
        BIGSERIAL character_id FK
    }

    npc_notes {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL note_id FK
        BIGSERIAL npc_id FK
        BIGSERIAL author_id FK
    }

    npc_visibility {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL npc_id FK
        BIGSERIAL player_id FK
    }

    books {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR title
        TEXT summary
        VARCHAR section
        VARCHAR language
        BOOLEAN is_hidden
        TEXT image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    maps {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR title
        TEXT image_url
    }

    monsters {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        VARCHAR size
        VARCHAR alignment
        INT armor_class
        INT hit_points
        VARCHAR speed
        JSONB abilities
        JSONB actions
        INT experience_points
        INT strength
        INT dexterity
        INT constitution
        INT intelligence
        INT wisdom
        INT charisma
        TEXT description
        TEXT image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    news {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR headline
        TEXT body
        news_category category
        TIMESTAMP game_datetime
        TEXT image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    calendar_events {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR title
        TEXT description
        TIMESTAMP game_datetime
        BOOLEAN is_exam
        calendar_event_type event_type
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    spells {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR name
        INT level
        JSONB cast_modes
        TEXT description
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    stories {
        BIGSERIAL id PK
        UUID external_id UK
        VARCHAR title
        TEXT content
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    student_scoreboard {
        BIGSERIAL id PK
        UUID external_id UK
        INT ranking
        VARCHAR student_name
        VARCHAR student_college
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    character_classes {
        BIGSERIAL id PK
        UUID external_id UK
        BIGSERIAL character_id FK
    }

    %% Relationships
    users ||--o{ player_characters : owns
    users ||--o{ notes : authors
    users ||--o{ npc_notes : authors
    users ||--o{ npc_visibility : "can see"

    colleges ||--o{ player_characters : belongs_to
    colleges ||--o{ npcs : belongs_to
    colleges ||--o{ classes : offers
    colleges ||--o{ clubs : has

    player_characters ||--o| character_sheet : has
    player_characters ||--o{ grades : receives
    player_characters ||--o{ character_clubs : "member of"
    player_characters ||--o{ inventory_items : owns
    player_characters ||--o{ item_identifications : discovers
    player_characters ||--o{ pets : owns
    player_characters ||--o{ tournament_results : participates
    player_characters ||--o{ npcs_reputation : "has reputation with"
    player_characters ||--o{ character_notes : "linked to"

    npcs ||--o{ class_professors : teaches
    npcs ||--o{ quests : responsible_for
    npcs ||--o{ npcs_reputation : "reputation from"
    npcs ||--o{ npc_notes : "linked to"
    npcs ||--o{ npc_visibility : "visible to"

    classes ||--o{ class_professors : "taught by"
    classes ||--o{ grades : "grades for"

    clubs ||--o{ character_clubs : "has members"

    stores ||--o{ store_items : sells

    store_items ||--o{ inventory_items : "in inventory"
    store_items ||--o{ item_identifications : identified

    tournaments ||--o{ tournament_results : results

    notes ||--o{ character_notes : "linked to character"
    notes ||--o{ npc_notes : "linked to npc"
```
