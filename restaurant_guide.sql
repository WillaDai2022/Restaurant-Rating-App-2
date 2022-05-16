--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6 (Ubuntu 13.6-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.6 (Ubuntu 13.6-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account; Type: TABLE; Schema: public; Owner: wei
--

CREATE TABLE public.account (
    account_id integer NOT NULL,
    password character varying NOT NULL,
    email character varying NOT NULL,
    phone character varying(20) NOT NULL,
    fname character varying(50) NOT NULL,
    lname character varying(50) NOT NULL,
    photo character varying
);


ALTER TABLE public.account OWNER TO wei;

--
-- Name: account_account_id_seq; Type: SEQUENCE; Schema: public; Owner: wei
--

CREATE SEQUENCE public.account_account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_account_id_seq OWNER TO wei;

--
-- Name: account_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wei
--

ALTER SEQUENCE public.account_account_id_seq OWNED BY public.account.account_id;


--
-- Name: fav_rest; Type: TABLE; Schema: public; Owner: wei
--

CREATE TABLE public.fav_rest (
    id integer NOT NULL,
    account_id integer NOT NULL,
    restaurant_id integer NOT NULL
);


ALTER TABLE public.fav_rest OWNER TO wei;

--
-- Name: fav_rest_id_seq; Type: SEQUENCE; Schema: public; Owner: wei
--

CREATE SEQUENCE public.fav_rest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fav_rest_id_seq OWNER TO wei;

--
-- Name: fav_rest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wei
--

ALTER SEQUENCE public.fav_rest_id_seq OWNED BY public.fav_rest.id;


--
-- Name: rating; Type: TABLE; Schema: public; Owner: wei
--

CREATE TABLE public.rating (
    rating_id integer NOT NULL,
    title character varying(100),
    pic text,
    score integer NOT NULL,
    review text,
    yelp_id character varying,
    account_id integer NOT NULL
);


ALTER TABLE public.rating OWNER TO wei;

--
-- Name: rating_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: wei
--

CREATE SEQUENCE public.rating_rating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rating_rating_id_seq OWNER TO wei;

--
-- Name: rating_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wei
--

ALTER SEQUENCE public.rating_rating_id_seq OWNED BY public.rating.rating_id;


--
-- Name: restaurant; Type: TABLE; Schema: public; Owner: wei
--

CREATE TABLE public.restaurant (
    restaurant_id integer NOT NULL,
    yelp_id character varying NOT NULL,
    name character varying NOT NULL,
    address character varying,
    url character varying
);


ALTER TABLE public.restaurant OWNER TO wei;

--
-- Name: restaurant_restaurant_id_seq; Type: SEQUENCE; Schema: public; Owner: wei
--

CREATE SEQUENCE public.restaurant_restaurant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_restaurant_id_seq OWNER TO wei;

--
-- Name: restaurant_restaurant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wei
--

ALTER SEQUENCE public.restaurant_restaurant_id_seq OWNED BY public.restaurant.restaurant_id;


--
-- Name: account account_id; Type: DEFAULT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.account ALTER COLUMN account_id SET DEFAULT nextval('public.account_account_id_seq'::regclass);


--
-- Name: fav_rest id; Type: DEFAULT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.fav_rest ALTER COLUMN id SET DEFAULT nextval('public.fav_rest_id_seq'::regclass);


--
-- Name: rating rating_id; Type: DEFAULT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.rating ALTER COLUMN rating_id SET DEFAULT nextval('public.rating_rating_id_seq'::regclass);


--
-- Name: restaurant restaurant_id; Type: DEFAULT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.restaurant ALTER COLUMN restaurant_id SET DEFAULT nextval('public.restaurant_restaurant_id_seq'::regclass);


--
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: wei
--

COPY public.account (account_id, password, email, phone, fname, lname, photo) FROM stdin;
1	12345678	donald_johnson@gmail.com	980-234-1343	Donald	Johnson	/static/image/backgrounds/no-photo.png
2	12345678	Vernice@gmail.com	980-257-5643	Vernice	Edwards	/static/image/backgrounds/no-photo.png
3	12345678	Jane@gmail.com	980-258-5343	Jane	Roberson	/static/image/backgrounds/no-photo.png
4	12345678	andrew@gmail.com	980-111-5343	Andrew	McDowell	/static/image/backgrounds/no-photo.png
5	12345678	Iona@gmail.com	980-121-5343	Iona	Love	/static/image/backgrounds/no-photo.png
6	12345678	Mark@gmail.com	980-348-5343	Mark	Gardner	/static/image/backgrounds/no-photo.png
7	12345678	Mark@gmail.com	980-348-5343	Mark	Gardner	/static/image/backgrounds/no-photo.png
8	12345678	Tom@gmail.com	980-348-5097	Tom	Rice	/static/image/backgrounds/no-photo.png
9	12345678	tester@gmail.com	980-348-5297	Mary	King	https://res.cloudinary.com/djyfl2zja/image/upload/v1652581857/d0bxaimiekzvgojtugee.jpg
10	12345678	tester1@gmail.com	980-291-1810	Joe	Williams	https://res.cloudinary.com/djyfl2zja/image/upload/v1652675787/iqck8rmqhspflrgfpeut.jpg
\.


--
-- Data for Name: fav_rest; Type: TABLE DATA; Schema: public; Owner: wei
--

COPY public.fav_rest (id, account_id, restaurant_id) FROM stdin;
\.


--
-- Data for Name: rating; Type: TABLE DATA; Schema: public; Owner: wei
--

COPY public.rating (rating_id, title, pic, score, review, yelp_id, account_id) FROM stdin;
1	123	https://res.cloudinary.com/djyfl2zja/image/upload/v1652581841/fzdm3fcnntmajwo5ijac.jpg	5	12345678	Lu5hB_5YtX5Re2067Zf3cg	9
2	Casual, friendly	https://res.cloudinary.com/djyfl2zja/image/upload/v1652675554/bxzg2es5otksiabjxufk.jpg	5	It’s a casual, friendly cafe with something for everybody. Great variety in the menu. I loved the beet and burrata salad.	hggVnGwA5042-ABxqeJX-A	10
\.


--
-- Data for Name: restaurant; Type: TABLE DATA; Schema: public; Owner: wei
--

COPY public.restaurant (restaurant_id, yelp_id, name, address, url) FROM stdin;
1	CcRA-ZFX2-vaUOJhg0Yj-Q	Three Amigos Mexican Kitchen & Cantina	7741 Colony Rd Ste A1	https://s3-media2.fl.yelpcdn.com/bphoto/2ejP3-HIuiPupWiVaprZDA/o.jpg
2	yxLVwItd1Wnhy6SeUUcNYA	The Lodge: A Sportsman's Grill	7725 Colony Rd Charlotte, NC 28226	https://s3-media3.fl.yelpcdn.com/bphoto/zo1spbszXF_gVDVTh2Quow/o.jpg
3	Cv5QcuX-gjU2Uio3CQbQpA	Sanctuary Bistro	6414 Rea Rd Ste C2	https://s3-media4.fl.yelpcdn.com/bphoto/IS1s76ukSeGW1eJio2OSVQ/o.jpg
4	caN0y8Ikt6F_7Ot8Nrkplg	Harry’s Grille & Tavern	8426 Park Rd Charlotte, NC 28210	https://s3-media3.fl.yelpcdn.com/bphoto/pLWYb2KnULhqRUSvTZeKeQ/o.jpg
5	zIELz5s9LknJgaawrwg0Zg	What The Fries	10707 Park Rd Ste F	https://s3-media1.fl.yelpcdn.com/bphoto/oUlWwUlVRbu7GNKAaTeF5g/o.jpg
6	_JgoEtpN2-wd9laXS8bGEg	bit	721 Governor Morrison St Ste 150	https://s3-media3.fl.yelpcdn.com/bphoto/wm2ohN6V0XFSOmiF7kR2sA/o.jpg
7	hggVnGwA5042-ABxqeJX-A	Good Food on Montford	1701 Montford Dr Charlotte, NC 28209	https://s3-media4.fl.yelpcdn.com/bphoto/M1OGHU_RvZ7qxf_FnZFuxQ/o.jpg
8	rnPPn7LTM9yuqkx7Gg9U6A	Char Bar No 7	4130 Carmel Rd Charlotte, NC 28226	https://s3-media2.fl.yelpcdn.com/bphoto/-U_m0BgiOPIHRt1MgT8BZw/o.jpg
\.


--
-- Name: account_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wei
--

SELECT pg_catalog.setval('public.account_account_id_seq', 10, true);


--
-- Name: fav_rest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wei
--

SELECT pg_catalog.setval('public.fav_rest_id_seq', 11, true);


--
-- Name: rating_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wei
--

SELECT pg_catalog.setval('public.rating_rating_id_seq', 2, true);


--
-- Name: restaurant_restaurant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wei
--

SELECT pg_catalog.setval('public.restaurant_restaurant_id_seq', 8, true);


--
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (account_id);


--
-- Name: fav_rest fav_rest_pkey; Type: CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.fav_rest
    ADD CONSTRAINT fav_rest_pkey PRIMARY KEY (id);


--
-- Name: rating rating_pkey; Type: CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_pkey PRIMARY KEY (rating_id);


--
-- Name: restaurant restaurant_pkey; Type: CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.restaurant
    ADD CONSTRAINT restaurant_pkey PRIMARY KEY (restaurant_id);


--
-- Name: fav_rest fav_rest_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.fav_rest
    ADD CONSTRAINT fav_rest_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.account(account_id);


--
-- Name: fav_rest fav_rest_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.fav_rest
    ADD CONSTRAINT fav_rest_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurant(restaurant_id);


--
-- Name: rating rating_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wei
--

ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.account(account_id);


--
-- PostgreSQL database dump complete
--

