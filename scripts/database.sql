-- Habilitar extensão para geração de UUIDs
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TYPE user_role AS ENUM ('DM', 'PLAYER');

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role user_role NOT NULL,
    avatar_url TEXT
);

CREATE TABLE colleges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    image_url TEXT
);

CREATE TABLE classes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    college_id UUID REFERENCES colleges(id) ON DELETE SET NULL,
    image_url TEXT
);

CREATE TABLE player_characters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    image_url TEXT,
    college_year INT,
    college_id UUID REFERENCES colleges(id) ON DELETE SET NULL,
    enrolled_classes TEXT,
    level INT
);

CREATE TABLE inventory_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    item_id UUID DEFAULT gen_random_uuid(),
    amount INT,
    metadata JSONB
);

CREATE TABLE character_sheet (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    proficiency_bonus INTEGER,
    armor_class INTEGER,
    initiative INTEGER,
    speed FLOAT,
    max_hit_points INTEGER,
    current_hit_points INTEGER,
    temp_hit_points INTEGER,
    hit_dice_total INTEGER,
    hit_dice_current INTEGER,
    save_str INTEGER,
    save_dex INTEGER,
    save_con INTEGER,
    save_int INTEGER,
    save_wis INTEGER,
    save_cha INTEGER,
    skills TEXT,
    background TEXT,
    race TEXT,
    alignment TEXT,
    experience_points INTEGER,
    languages TEXT,
    features_traits TEXT,
    proficiencies TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE npcs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    image_url TEXT,
    bio TEXT,
    is_visible BOOLEAN DEFAULT TRUE,
    visible_to TEXT
);

CREATE TABLE npcs_reputation (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    npc_id UUID REFERENCES npcs(id) ON DELETE CASCADE,
    score INT
);

CREATE TABLE notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    author_id UUID REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    is_master_only BOOLEAN DEFAULT FALSE,
    is_privative BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE character_notes (
    note_id UUID REFERENCES notes(id) ON DELETE CASCADE,
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    PRIMARY KEY (note_id, character_id)
);

CREATE TABLE npc_notes (
    note_id UUID REFERENCES notes(id) ON DELETE CASCADE,
    npc_id UUID REFERENCES npcs(id) ON DELETE CASCADE,
    author_id UUID REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (note_id, npc_id)
);

CREATE TABLE calendar_notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    game_datetime TIMESTAMP,
    is_exam BOOLEAN DEFAULT FALSE
);

CREATE TABLE event_notes (
    note_id UUID REFERENCES notes(id) ON DELETE CASCADE,
    event_id UUID REFERENCES calendar_notes(id) ON DELETE CASCADE,
    author_id UUID REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (note_id, event_id)
);

CREATE TABLE stores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    description TEXT,
    image_url TEXT
);

CREATE TABLE store_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    store_id UUID REFERENCES stores(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    image_url TEXT
);

CREATE TABLE books (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    summary TEXT,
    section VARCHAR(255),
    is_hidden BOOLEAN DEFAULT FALSE,
    image_url TEXT
);

CREATE TABLE news (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    headline VARCHAR(255) NOT NULL,
    body TEXT,
    game_datetime TIMESTAMP,
    image_url TEXT
);

CREATE TABLE maps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    image_url TEXT
);

CREATE TABLE monsters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    hit_points INT,
    experience_points INT,
    strength INT,
    dexterity INT,
    constitution INT,
    intelligence INT,
    wisdom INT,
    charisma INT,
    armor_class INT,
    description TEXT,
    image_url TEXT
);

CREATE TABLE sessions (
    session_id TEXT PRIMARY KEY,
    user_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP NOT NULL
);
