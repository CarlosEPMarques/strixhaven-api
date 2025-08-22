# Data Model

## Enumerations

### `user_role`

- Possible values: `'DM'`, `'PLAYER'`

### `news_category`

- Possible values: `'EVENT'`, `'ANNOUNCEMENT'`, `'UPDATE'`, `'OTHER'`

### `calendar_event_type`

- Possible values: `'CLASS'`, `'EXAM'`, `'HOLIDAY'`, `'OTHER'`

### `store_item_rarity`

- Possible values: `'COMMON'`, `'UNCOMMON'`, `'RARE'`, `'EPIC'`, `'LEGENDARY'`

### `npc_occupation`

- Possible values: `'PROFESSOR'`, `'STUDENT'`, `'MERCHANT'`, `'OTHER'`

---

## Tables

### `users`

| Column     | Type        | Constraints      | Description                |
| ---------- | ----------- | ---------------- | -------------------------- |
| id         | UUID        | PK               | Unique user identifier     |
| name       | VARCHAR(100)| NOT NULL         | User's name                |
| email      | VARCHAR(100)| UNIQUE, NOT NULL | User's email               |
| password   | VARCHAR(255)| NOT NULL         | User's password            |
| role       | `user_role` | NOT NULL         | User's role                |
| avatar_url | TEXT        |                  | URL to user's avatar image |
| created_at | TIMESTAMP   | DEFAULT NOW()    | Creation timestamp         |
| updated_at | TIMESTAMP   | DEFAULT NOW()    | Update timestamp           |

---

### `colleges`

| Column       | Type         | Constraints   | Description          |
| ------------ | ------------ | ------------- | -------------------- |
| id           | UUID         | PK            | College identifier   |
| name         | VARCHAR(100) | NOT NULL      | College name         |
| description  | TEXT         |               | College description  |
| image_url    | TEXT         |               | URL to college image |
| founded_year | INT          |               | Year college founded |
| traditions   | JSONB        |               | College traditions   |
| created_at   | TIMESTAMP    | DEFAULT NOW() | Creation timestamp   |
| updated_at   | TIMESTAMP    | DEFAULT NOW() | Update timestamp     |

---

### `books`

| Column     | Type         | Constraints   | Description        |
| ---------- | ------------ | ------------- | ------------------ |
| id         | UUID         | PK            | Book identifier    |
| title      | VARCHAR(100) | NOT NULL      | Book title         |
| summary    | TEXT         |               | Book summary       |
| section    | VARCHAR(100) |               | Book section       |
| language   | VARCHAR(50)  |               | Book language      |
| is_hidden  | BOOLEAN      | DEFAULT FALSE | Visibility flag    |
| image_url  | TEXT         |               | Book image URL     |
| created_at | TIMESTAMP    | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP    | DEFAULT NOW() | Update timestamp   |

---

### `maps`

| Column    | Type         | Constraints | Description    |
| --------- | ------------ | ----------- | -------------- |
| id        | UUID         | PK          | Map identifier |
| title     | VARCHAR(100) | NOT NULL    | Map title      |
| image_url | TEXT         |             | Map image URL  |

---

### `monsters`

| Column            | Type         | Constraints   | Description         |
| ----------------- | ------------ | ------------- | ------------------- |
| id                | UUID         | PK            | Monster identifier  |
| name              | VARCHAR(100) | NOT NULL      | Monster name        |
| size              | VARCHAR(50)  |               | Monster size        |
| alignment         | VARCHAR(50)  |               | Alignment           |
| armor_class       | INT          |               | Armor Class         |
| hit_points        | INT          |               | Hit Points          |
| speed             | VARCHAR(50)  |               | Movement speed      |
| abilities         | JSONB        |               | Monster abilities   |
| actions           | JSONB        |               | Monster actions     |
| experience_points | INT          |               | Experience points   |
| strength          | INT          |               | Strength            |
| dexterity         | INT          |               | Dexterity           |
| constitution      | INT          |               | Constitution        |
| intelligence      | INT          |               | Intelligence        |
| wisdom            | INT          |               | Wisdom              |
| charisma          | INT          |               | Charisma            |
| description       | TEXT         |               | Monster description |
| image_url         | TEXT         |               | Monster image URL   |
| created_at        | TIMESTAMP    | DEFAULT NOW() | Creation timestamp  |
| updated_at        | TIMESTAMP    | DEFAULT NOW() | Update timestamp    |

---

### `news`

| Column        | Type           | Constraints   | Description        |
| ------------- | -------------- | ------------- | ------------------ |
| id            | UUID           | PK            | News identifier    |
| headline      | VARCHAR(100)   | NOT NULL      | News headline      |
| body          | TEXT           |               | News body          |
| category      | `news_category`|               | News category      |
| game_datetime | TIMESTAMP      |               | In-game date/time  |
| image_url     | TEXT           |               | News image URL     |
| created_at    | TIMESTAMP      | DEFAULT NOW() | Creation timestamp |
| updated_at    | TIMESTAMP      | DEFAULT NOW() | Update timestamp   |

---

### `calendar_events`

| Column        | Type                 | Constraints   | Description        |
| ------------- | ------------------- | ------------- | ------------------ |
| id            | UUID                 | PK            | Event identifier   |
| title         | VARCHAR(100)         | NOT NULL      | Event title        |
| description   | TEXT                 |               | Event description  |
| game_datetime | TIMESTAMP            |               | In-game date/time  |
| is_exam       | BOOLEAN              | DEFAULT FALSE | Exam flag          |
| event_type    | `calendar_event_type`|               | Type of event      |
| created_at    | TIMESTAMP            | DEFAULT NOW() | Creation timestamp |
| updated_at    | TIMESTAMP            | DEFAULT NOW() | Update timestamp   |

---

### `npcs`

| Column       | Type               | Constraints                             | Description          |
| ------------ | ----------------- | --------------------------------------- | ------------------  |
| id           | UUID               | PK                                      | NPC identifier       |
| name         | VARCHAR(100)       | NOT NULL                                | NPC name             |
| college_id   | UUID               | FK to `colleges(id)` ON DELETE SET NULL | NPC's college        |
| college_year | INT                |                                         | NPC's college year   |
| image_url    | TEXT               |                                         | NPC image URL        |
| bio          | TEXT               |                                         | NPC biography        |
| occupation   | `npc_occupation`   |                                         | NPC occupation       |
| personality  | JSONB              |                                         | NPC personality      |
| location     | VARCHAR(100)       |                                         | NPC location         |
| is_visible   | BOOLEAN            | DEFAULT TRUE                            | Visibility flag      |
| created_at   | TIMESTAMP          | DEFAULT NOW()                           | Creation timestamp   |
| updated_at   | TIMESTAMP          | DEFAULT NOW()                           | Update timestamp     |

---

### `player_characters`

| Column       | Type         | Constraints                             | Description          |
| ------------ | ------------ | --------------------------------------- | --------------------|
| id           | UUID         | PK                                      | Character identifier |
| user_id      | UUID         | FK to `users(id)` ON DELETE CASCADE     | Owning user          |
| name         | VARCHAR(100) | NOT NULL                                | Character name       |
| image_url    | TEXT         |                                         | Character image URL  |
| college_year | INT          |                                         | College year         |
| college_id   | UUID         | FK to `colleges(id)` ON DELETE SET NULL | Character's college  |
| level        | INT          |                                         | Character level      |
| goals        | TEXT         |                                         | Character goals      |
| hobbies      | JSONB        |                                         | Character hobbies    |
| allies       | JSONB        |                                         | Allies               |
| enemies      | JSONB        |                                         | Enemies              |
| created_at   | TIMESTAMP    | DEFAULT NOW()                           | Creation timestamp   |
| updated_at   | TIMESTAMP    | DEFAULT NOW()                           | Update timestamp     |

---

### `classes`

| Column      | Type         | Constraints                             | Description        |
| ----------- | ------------ | --------------------------------------- | ------------------ |
| id          | UUID         | PK                                      | Class identifier   |
| name        | VARCHAR(100) | NOT NULL                                | Class name         |
| description | TEXT         |                                         | Class description  |
| college_id  | UUID         | FK to `colleges(id)` ON DELETE SET NULL | Associated college |
| image_url   | TEXT         |                                         | Class image URL    |
| created_at  | TIMESTAMP    | DEFAULT NOW()                           | Creation timestamp |
| updated_at  | TIMESTAMP    | DEFAULT NOW()                           | Update timestamp   |

---

### `class_professors`

| Column   | Type | Constraints                         | Description        |
| -------- | ---- | ----------------------------------- | ------------------ |
| class_id | UUID | FK to `classes(id)` ON DELETE CASCADE | Associated class  |
| npc_id   | UUID | FK to `npcs(id)` ON DELETE CASCADE    | Professor NPC     |

**Primary Key:** (class_id, npc_id)

---

## Mermaid Diagram

```mermaid
erDiagram

    %% =========================
    %% USERS & AUTHENTICATION
    %% =========================
    USERS {
        uuid id PK
        string name
        string email
        string password
        enum role
        text avatar_url
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% COLLEGES & CAMPAIGN STRUCTURE
    %% =========================
    COLLEGES {
        uuid id PK
        string name
        text description
        text image_url
        int founded_year
        jsonb traditions
        timestamp created_at
        timestamp updated_at
    }

    CLASSES {
        uuid id PK
        string name
        text description
        uuid college_id FK
        text image_url
        timestamp created_at
        timestamp updated_at
    }

    PLAYER_CHARACTERS {
        uuid id PK
        uuid user_id FK
        string name
        text image_url
        int college_year
        uuid college_id FK
        int level
        text goals
        jsonb hobbies
        jsonb allies
        jsonb enemies
        timestamp created_at
        timestamp updated_at
    }

    CHARACTER_SHEET {
        uuid id PK
        uuid character_id FK
        int strength
        int dexterity
        int constitution
        int intelligence
        int wisdom
        int charisma
        int proficiency_bonus
        int armor_class
        int initiative
        int speed
        int max_hit_points
        int current_hit_points
        int temp_hit_points
        int hit_dice_total
        int hit_dice_current
        int save_str
        int save_dex
        int save_con
        int save_int
        int save_wis
        int save_cha
        jsonb skills
        text background
        text race
        text alignment
        int experience_points
        jsonb languages
        jsonb features_traits
        jsonb proficiencies
        text description
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% INVENTORY & ITEMS
    %% =========================
    INVENTORY_ITEMS {
        uuid id PK
        uuid character_id FK
        uuid item_id FK
        int amount
        jsonb metadata
        timestamp created_at
        timestamp updated_at
    }

    STORE_ITEMS {
        uuid id PK
        uuid store_id FK
        string name
        text description
        decimal price
        enum rarity
        int durability
        text lore
        text image_url
        timestamp created_at
        timestamp updated_at
    }

    STORES {
        uuid id PK
        string name
        string location
        text description
        text image_url
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% NPCs & REPUTATION
    %% =========================
    NPCS {
        uuid id PK
        string name
        uuid college_id FK
        int college_year
        text image_url
        text bio
        enum occupation
        jsonb personality
        string location
        boolean is_visible
        timestamp created_at
        timestamp updated_at
    }

    NPCS_REPUTATION {
        uuid id PK
        uuid character_id FK
        uuid npc_id FK
        int score
        timestamp created_at
        timestamp updated_at
    }

    NPC_VISIBILITY {
        uuid npc_id FK
        uuid player_id FK
    }

    %% =========================
    %% NOTES SYSTEM
    %% =========================
    NOTES {
        uuid id PK
        uuid author_id FK
        string title
        text content
        boolean is_master_only
        timestamp created_at
        timestamp updated_at
    }

    CHARACTER_NOTES {
        uuid note_id FK
        uuid character_id FK
    }

    NPC_NOTES {
        uuid note_id FK
        uuid npc_id FK
        uuid author_id FK
    }

    %% =========================
    %% CALENDAR EVENTS
    %% =========================
    CALENDAR_EVENTS {
        uuid id PK
        string title
        text description
        timestamp game_datetime
        boolean is_exam
        enum event_type
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% QUESTS, SPELLS & STORIES
    %% =========================
    QUESTS {
        uuid id PK
        string title
        text description
        uuid responsible_npc FK
        boolean active
        jsonb rewards
        timestamp expire_date
        timestamp created_at
        timestamp updated_at
    }

    SPELLS {
        uuid id PK
        string name
        int level
        jsonb cast_modes
        text description
        timestamp created_at
        timestamp updated_at
    }

    STORIES {
        uuid id PK
        string title
        text content
        timestamp created_at
        timestamp updated_at
    }

    STUDENT_SCOREBOARD {
        uuid id PK
        int ranking
        string student_name
        string student_college
        timestamp created_at
        timestamp updated_at
    }

    CHARACTER_CLASSES {
        uuid character_id FK
        uuid class_id FK
    }

    GRADES {
        uuid id PK
        uuid character_id FK
        uuid class_id FK
        int score
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% BOOKS & NEWS
    %% =========================
    BOOKS {
        uuid id PK
        string title
        text summary
        string section
        string language
        boolean is_hidden
        text image_url
        timestamp created_at
        timestamp updated_at
    }

    NEWS {
        uuid id PK
        string headline
        text body
        enum category
        timestamp game_datetime
        text image_url
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% MAPS & MONSTERS
    %% =========================
    MAPS {
        uuid id PK
        string title
        text image_url
    }

    MONSTERS {
        uuid id PK
        string name
        string size
        string alignment
        int armor_class
        int hit_points
        string speed
        jsonb abilities
        jsonb actions
        int experience_points
        int strength
        int dexterity
        int constitution
        int intelligence
        int wisdom
        int charisma
        text description
        text image_url
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% RELATIONSHIPS
    %% =========================
    USERS ||--o{ PLAYER_CHARACTERS : "has"
    USERS ||--o{ NOTES : "writes"
    USERS ||--o{ NPC_NOTES : "writes"

    COLLEGES ||--o{ CLASSES : "offers"
    COLLEGES ||--o{ PLAYER_CHARACTERS : "attended by"
    COLLEGES ||--o{ NPCS : "hosts"

    CLASSES ||--o{ PLAYER_CHARACTERS : "enrolled in"
    CLASSES ||--o{ CHARACTER_CLASSES : "assigned to"
    CLASSES ||--o{ GRADES : "graded in"

    PLAYER_CHARACTERS ||--o{ CHARACTER_SHEET : "has"
    PLAYER_CHARACTERS ||--o{ INVENTORY_ITEMS : "owns"
    PLAYER_CHARACTERS ||--o{ NPCS_REPUTATION : "interacts with"
    PLAYER_CHARACTERS ||--o{ CHARACTER_NOTES : "has"
    PLAYER_CHARACTERS ||--o{ CHARACTER_CLASSES : "enrolled in"
    PLAYER_CHARACTERS ||--o{ GRADES : "receives"

    NPCS ||--o{ NPCS_REPUTATION : "linked to"
    NPCS ||--o{ NPC_NOTES : "has notes"
    NPCS ||--o{ QUESTS : "responsible for"
    NPCS ||--o{ NPC_VISIBILITY : "visible to"

    CALENDAR_EVENTS ||--o{ NOTES : "linked to"

    NOTES ||--o{ CHARACTER_NOTES : "relates to"
    NOTES ||--o{ NPC_NOTES : "relates to"

    STORES ||--o{ STORE_ITEMS : "sells"
    STORE_ITEMS ||--o{ INVENTORY_ITEMS : "owned by"

```
